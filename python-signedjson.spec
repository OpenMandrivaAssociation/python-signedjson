Name:		python-signedjson
Version:	1.1.4
Release:	4
Source0:	https://files.pythonhosted.org/packages/source/s/signedjson/signedjson-%{version}.tar.gz
Summary:	Sign JSON with Ed25519 signatures
URL:		https://pypi.org/project/signedjson/
License:	GPL
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildArch:	noarch

%description
Sign JSON with Ed25519 signatures

%files
%{py_sitedir}/signedjson
%{py_sitedir}/signedjson-%{version}.dist-info
