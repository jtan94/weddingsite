from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class RSVP(models.Model):
    rsvp_code = models.CharField(max_length=8)
    rsvp_name = models.CharField(max_length=200)
    additional_guests = models.IntegerField(default=0)

    def __str__(self):
        return self.rsvp_name


    #example Predefined Guests
    ##uniqueIdentifier = 12345dfd
    ##Name -> Tan Family
    ##InvitedGuests is an array :
        #[Guest = {name = Andrew Tan, RSVP = True, Dietary Restrictions = False}, Guest = {name = Camille Tan, RSVP= False, Dietary Restrictions = False}]
    ##AdditionalGuests=0
    #example of AddIn Guests
    ##uniqueIdentifier = 1235de
    ##Name -> Kathy Salazar
    ##InvitedGuests = [Guest = {name = Kathy Salazar, RSVP= True, Dietary Restrictions = False}]
    ##AdditionalGuests = 1 (when this field != 0, will be prompted to add a guest, if they decline the RSVP finishes, else prompted to enter guests name and dietary restrictions)


class InvitedGuest(models.Model):
    rsvpModel = models.ForeignKey(RSVP, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=200)
    rsvp = models.BooleanField(default=False)
    dietary_restrictions = models.BooleanField(default=False)

    def __str__(self):
        return self.guest_name


