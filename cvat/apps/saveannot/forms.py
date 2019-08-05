from django import forms
class AnnotationListForm(forms.Form):
    annotationformat = forms.ChoiceField(label="Select the annotation format",choices=[(1,"VOC"),(2,"YOLO")])
    def __init__(self, *args, **kwargs):
        annotchoices = kwargs.pop('choices')
        super(AnnotationListForm, self).__init__(*args, **kwargs)
        self.fields['tasks']=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label="Select the tasks to download\n",choices=annotchoices)



class DownloadListForm(forms.Form):
    annotationformat = forms.ChoiceField(label="Select the annotation format",choices=[(1,"VOC"),(2,"YOLO")])
    def __init__(self, *args, **kwargs):
        annotchoices = kwargs.pop('choices')
        super(AnnotationListForm, self).__init__(*args, **kwargs)
        self.fields['tasks']=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label="Select the tasks to download\n",choices=annotchoices)


