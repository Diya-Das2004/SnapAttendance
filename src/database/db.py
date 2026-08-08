from src.database.config import supabase

import bcrypt

def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(),bcrypt.gensalt()).decode()
def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(),hashed.encode())

def check_teacher_exists(username):
    # check for unique username ,returns false when same username is given
    responses= supabase.table("teachers").select("username").eq("username",username).execute()
    return len(responses.data) > 0

def create_teacher(username,password, name):
    data={"username": username,"password": hash_pass(password),"name": name}
    responses= supabase.table("teachers").insert(data).execute()
    return responses.data

def teacher_login(username,password):
    responses = supabase.table("teachers").select("*").eq("username",username).execute() #* mane sb data chai oi table er
    if responses.data:
        teacher= responses.data[0]
        if check_pass(password,teacher['password']):
            return teacher
    return None
def get_all_students():
    responses= supabase.table("students").select("*").execute()  
    return responses.data

def create_student(new_name, face_embeddings=None, voice_embeddings=None):
    data= {'name': new_name,'face_embeddings':face_embeddings,'voice_embeddings':voice_embeddings}
    response= supabase.table('students').insert(data).execute()
    return response.data

def create_subject( teacher_id,sub_id, sub_name, sub_Section):
    data={"teacher_id":teacher_id,"subject_code": sub_id,"name":sub_name,"section":sub_Section}
    response= supabase.table("subjects").insert(data).execute()
    return response.data

def get_teacher_subjects(teacher_id):
    response= supabase.table('subjects').select('*, subject_students(count),attendence_logs(timestamp)').eq("teacher_id", teacher_id).execute()
    subjects= response.data

    for sub in subjects:
        sub['total_students']= sub.get("subject_students",[{}])[0].get('count',0)if sub.get('subject_students') else 0
        attendence= sub.get('attendence_logs',[])
        unique_sessions= len(set(log['timestamp'] for log in attendence))
        sub['total_classes']= unique_sessions

        sub.pop('subject_student', None)
        sub.pop('attendence_logs', None)

    return subjects

def enroll_student_to_subject(student_id,subject_id):
    data={"student_id":student_id,"subject_id" : subject_id}
    response= supabase.table('subject_students').insert(data).execute()
    return response.data

def unenroll_student_to_subject(student_id,subject_id):
    response= supabase.table('subject_students').delete().eq('student_id', student_id).eq('subject_id',subject_id).execute()
    return response.data 

def get_student_subjects(student_id):
    response= supabase.table('subject_students').select('*,subjects(*)').eq('student_id', student_id).execute()
    return response.data

def get_student_attendence(student_id):
    response= supabase.table('attendence_logs').select('*,subjects(*)').eq('student_id', student_id).execute()
    return response.data

def create_attendence(logs):
    response= supabase.table('attendence_logs').insert(logs).execute()
    return response.data

def get_attendence_for_teachers(teacher_id):
    response = supabase.table('attendence_logs').select("*, subjects!inner(*)").eq('subjects.teacher_id', teacher_id).execute()
    return response.data
    