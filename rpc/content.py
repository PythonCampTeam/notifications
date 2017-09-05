from jinja2 import Environment, PackageLoader
from sendgrid.helpers.mail import Content


def email_content(name, label=None, order=None):
    """This method create template for email
    Args:
        name (str): Name of customer.
        label (str): link to label.
        order: order of customer

    Return:
        content (html): Temaplate of mail.
    """
    if order:
        ENV = Environment(loader=PackageLoader(
                                        'notifications.config',
                                        'templates'
                                              )
                          )
        template = ENV.get_template('email_template.html')
        context = {
                    'name': name,
                    'label': label,
                    'order_id': order.id,
                    'order_items': order['items']
                   }
        content = template.render(context)

        content = Content('text/html', content)
        return content
    return None
