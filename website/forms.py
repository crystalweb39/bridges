from django import forms
from bridges.website.models import *

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        
    confirm_email = forms.EmailField(error_messages={'required':'Please confirm your Email Address'})

        
    def __init__(self, *args, **kwargs):
        super(EnquiryForm, self).__init__(*args, **kwargs)
        self.fields['firstname'].error_messages = {'required':'Please enter your First Name'}
        self.fields['lastname'].error_messages = {'required':'Please enter your Last Name'}
        self.fields['email'].error_messages = {'required':'Please enter your Email Address'}
        self.fields['phone'].error_messages = {'required':'Please enter your Phone Number'}
        self.fields['comment'].error_messages = {'required':'Please enter your Message'}
        
    def clean_confirm_email(self):
        if self.data.get('email','') and self.data.get('confirm_email',''):
            if self.data.get('email','') != self.data.get('confirm_email',''):
                raise forms.ValidationError("Email addresses do not match")
            
        return self.cleaned_data.get('confirm_email','')