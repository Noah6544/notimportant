from django import forms


class getUserInfoForm(forms.Form):
    email = forms.EmailField()
    os = forms.ChoiceField(
        choices=(
            ('windows', 'Windows'),
            ('mac', 'Mac OS X'),
            ('linux', 'Linux'),
        )
    )




    # subject = forms.CharField(
    #     max_length=100,
    #     label='Email subject',
    #     widget=forms.TextInput(attrs={'placeholder': 'Enter the subject here'})
    # )
    # message = forms.CharField(
    #     widget=forms.Textarea(attrs={'placeholder': 'Enter your message here'}),
    #     label='Your message'
    # )
    # sender = forms.EmailField(
    #     label='Your email address',
    #     widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address'})
    # )
    # cc_myself = forms.BooleanField(
    #     required=False,  # Checkbox is optional
    #     label='CC yourself?'
    # )