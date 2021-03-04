from setuptools import setup
import versioneer

setup(
    name="libmorphocluster",
    packages=["libmorphocluster"],
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    include_package_data=True,
    install_requires=["pandas",],
    extras_require={"tests": ["pytest", "pytest-cov"],},
)
