from setuptools import find_packages, setup

package_name = 'rosbot_py_examples'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Fernando Filho',
    maintainer_email='fernando.rsf23@gmail.com',
    description='ROS2 Python examples for ROSbot',
    license='MIT License',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'simple_publisher = rosbot_py_examples.simple_publisher:main'
        ],
    },
)
