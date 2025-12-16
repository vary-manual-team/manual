
import sys
import pkg_resources

installed_packages = {pkg.key for pkg in pkg_resources.working_set}
print(f"pypdf in installed: {'pypdf' in installed_packages}")
print(f"pdfminer in installed: {'pdfminer' in installed_packages or 'pdfminer.six' in installed_packages}")
