from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np
import streamlit as st
import io
import librosa


@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder()

def get_voice_embeddings(audio_bytes):
    try:
        encoder= load_voice_encoder()
        audio,sr= librosa.load(io.BytesIO(audio_bytes),sr=1600)
        wav= preprocess_wav(audio)
        embeddings= encoder.embed_utterance(wav)
        return embeddings.tolist()
    except Exception as e:
        st.error('voice recog error')
        return None

def identity_speaker(new_embedding, candidates_dict, thresold=0.65):
    if new_embedding is None or not candidates_dict:
        return None,0.0

    best_student_id= None
    best_score= -1.0
    for student_id ,stored_embedding in candidates_dict.items():
        if stored_embedding:
            similarity= np.dot(new_embedding, stored_embedding)
            if similarity> best_score:
                best_score= similarity
                best_student_id= student_id
    if best_score>=thresold:
        return best_student_id, best_score
    
    return None, best_score

def process_bulk_audio(audio_bytes,candidates_dict, thresold=0.65):
    try:
        encoder= load_voice_encoder()
        audio, sr= librosa.load(io.BytesIO(audio_bytes),sr=16000)
        segment= librosa.effects.split(audio, top_db=30)
        identified_results={}

        for start,end in segment:
            if(end-start)< sr *0.5:
                continue
            segment_audio= audio[start:end]
            wav= preprocess_wav(segment_audio)
            embeddings= encoder.embed_utterance(wav)

            student_id, score= identity_speaker(embeddings,candidates_dict, thresold)
            if student_id:
                if student_id not in identified_results or score> identified_results[student_id]:
                    identified_results[student_id]= score
        return identified_results
    except Exception as e:
        st.error('Bulk processor error')
        return {}
            
           