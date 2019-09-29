from setuptools import setup

with open('pypi_desc.md') as f:
    long_description = f.read()


setup(
    name='pymata-aio',
    version='2.31',
    packages=['pymata_aio', 'utilities'],
    install_requires=['pyserial', 'websockets'],
    entry_points={
        'console_scripts': [
            'list_serial_ports = utilities.list_serial_ports:lsp',
        ]
    },
    url='https://github.com/MrYsLab/pymata-aio/wiki',
    download_url='https://github.com/MrYsLab/pymata-aio',
    license='GNU Affero General Public License v3 or later (AGPLv3+)',
    author='Alan Yorinks',
    author_email='MisterYsLab@gmail.com',
    description='A Python Protocol Abstraction Library For Arduino Firmata using Python asyncio',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['Firmata', 'Arduino', 'Protocol'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
        'Topic :: Education',
        'Topic :: Home Automation',
    ],
)

