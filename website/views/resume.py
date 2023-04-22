from django.shortcuts import render
from website.models.resume import Education, Experience, Certificates, SoftSkill, CodingSkill

def resume(request):
    education = Education.objects.all()
    experience = Experience.objects.all()
    certificates = Certificates.objects.all()
    softSkill = SoftSkill.objects.all()
    codingSkill = CodingSkill.objects.all()
    return render(request, 'resume.html', {
        'education': education, 'experience': experience, 'certificates': certificates, 'softSkill': softSkill,
        'codingSkill': codingSkill
    })
