from setuptools import find_packages, setup

# Note: format `dependency~=MAJOR.MINOR` ensures that only MAJOR version is locked.
install_requires = ["aiohttp>=3.2,<4"]

dev_requires = ["black==19.3b0", "flake8>=3.3", "isort==4.3.21", "pytest~=3.0"]


setup(
    name="amazon_wishlist",
    version="0.0.1",
    url="git@github.com:CarlosRasche/wishlist.git",
    author="Nacho&Carlos Rasche",
    author_email="nacho.rasche@gmail.com",
    description="Amazon wishlist server",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=install_requires,
    python_requires=">=3.5.3",
    setup_requires=["pytest-runner"],
    tests_require=dev_requires,
    extras_require={"dev": dev_requires},
)
