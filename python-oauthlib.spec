%define 	module	oauthlib

Summary:	OAuth Python implementation
Name:		python-%{module}
Version:	0.5.1
Release:	1
License:	BSD-like
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/o/oauthlib/%{module}-%{version}.tar.gz
# Source0-md5:	45ebbd43c9430bb404c9aa0979d949f2
URL:		https://github.com/sigmavirus24/charade
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A generic, spec-compliant, thorough implementation of the OAuth
request-signing logic.

%package -n python3-oauthlib
Summary:	OAuth Python implementation
Group:		Development/Languages/Python
Requires:	python3-modules

%description -n python3-oauthlib
A generic, spec-compliant, thorough implementation of the OAuth
request-signing logic.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build -b python
%{__python3} setup.py build -b python3

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py build -b python install \
	--optimize=2		\
	--root=$RPM_BUILD_ROOT	\
	--skip-build

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%{__python3} setup.py build -b python3 install \
	--optimize=2		\
	--root=$RPM_BUILD_ROOT	\
	--skip-build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/%{module}

%files -n python3-oauthlib
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/%{module}

