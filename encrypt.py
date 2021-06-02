import codecs

import click

@click.command()
# @click.option('--password', prompt=True, hide_input=True,
#               confirmation_prompt=True)
@click.password_option()
def encrypt(password):
    # click.echo('Encrypting password to %s' % password.encode('rot13'))
    click.echo('Encrypting password to %s' % codecs.encode(password, 'rot-13'))
