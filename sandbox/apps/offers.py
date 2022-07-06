from oscar.apps.offer import models


class ChangesOwnerName(models.Benefit):

    class Meta:
        proxy = True
        app_label = ''

    def apply(self, basket, condition, offer=None):
        condition.consume_items(offer, basket, ())
        return models.PostOrderAction(
            "You will have your name changed to Siri!")

    def apply_deferred(self, basket, order, application):
        if basket.owner:
            basket.owner.first_name = "Siri"
            basket.owner.save()
        return "Your name has been changed to Siri!"

    @property
    def description(self):
        return "Changes owners name"

    name = description
