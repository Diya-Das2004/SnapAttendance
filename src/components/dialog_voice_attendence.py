import streamlit as st
from src.database.config import supabase
from src.pipelines.voice_pipeline import process_bulk_audio
from datetime import datetime
import pandas as pd
from src.components.dialog_attendence_results import show_attendence_results

@st.dialog('Voice Attendence')

def voice_attendence_dialog(selected_subject_id):
    st.write('Record audio of students saying I am present . Then AI will recognize the students')

    audio_data= None
    audio_data= st.audio_input("Record classroom audio")
    if st.button('Analyze Audio', width='stretch',type='primary'):
        with st.spinner('Processing Audio data'):
            enrolled_res= supabase.table('subject_students').select("*, students(*)").eq('subject_id',selected_subject_id).execute()
            enrolled_students= enrolled_res.data
            if not enrolled_students:
                st.warning('No students enrolled in this course')
                return
            canditates_dict= {
                s['students']['student_id'] : s['students']['voice_embeddings']
                for s in enrolled_students if s['students'].get('voice_embeddings')

            }
            if not canditates_dict:
                st.error('No enrolled students has voice profiles registered')
                return
            audio_bytes= audio_data.read()
            detected_scores= process_bulk_audio(audio_bytes, canditates_dict)
            results, attendence_to_log =[],[]
            current_timestamp= datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

            for node in enrolled_students:
                student= node['students']
                score= detected_scores.get(student['student_id'],0.0)
                is_present = bool(score)>0

                results.append({
                    "Name": student['name'],
                    "ID": student['student_id'],
                    "Source": score if is_present else "-",
                    "Status": "Present" if is_present else "Absent"
                    })

                attendence_to_log.append({
                    'student_id': student['student_id'],
                    'subject_id': selected_subject_id,
                    'timestamp': current_timestamp,
                    'is_present': bool(is_present)
                })
            st.session_state.voice_embedding_results= (pd.DataFrame(results),attendence_to_log)

    if st.session_state.get('voice_embedding_results'):
        st.divider()
        df_results, logs= st.session_state.voice_embedding_results
        show_attendence_results(df_results,logs)