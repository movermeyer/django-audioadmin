# -*- coding: utf-8 -*-
import mimetypes
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

@deconstructible
class MimetypeValidator(object):
    def __init__(self, mimetypes):
        self.mimetypes = mimetypes
    
    def __call__(self, value):
        try:
            if not mimetypes.guess_type(value.path)[0] in self.mimetypes:
                raise ValidationError('%s is not an acceptable file type' % value)
        except AttributeError as e:
            raise ValidationError('This value could not be validated for file type' % value)