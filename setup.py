from setuptools import find_packages, setup

setup(
    name="pdf_annot",
    version="0.1.0",
    maintainer='Hongze Xia',
    maintainer_email='hongzex@gmail.com',
    author='Hongze Xia',
    url='https://github.com/xiahongze/pdf_annot',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    description='Utilities to extract and merge PDF annotations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='GPL-3',
    install_requires=[
        'python_version>=3.7',
        'PyMuPDF>=1.16'
    ]
)
