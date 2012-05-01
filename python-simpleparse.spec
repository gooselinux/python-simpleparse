%define oname   SimpleParse

Name:           python-simpleparse
License:        BSD
Group:          System Environment/Libraries
Summary:        A simple and fast parser generator
Version:        2.1.1
Release:        3%{?dist}
URL:            http://launchpad.net/simpleparse
Source0:        http://pypi.python.org/packages/source/S/SimpleParse/%{oname}-%{version}.tar.gz
Patch1:         %{name}-eols.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  python-devel

%description
SimpleParse is a BSD-licensed Python package providing a simple and fast parser
generator using a modified version of the mxTextTools text-tagging engine.
SimpleParse allows you to generate parsers directly from your EBNF grammar.


# we don't want to provide mxTextTools.so
%{?filter_setup:
%filter_provides_in %{python_sitearch}/.*\.so$ 
%filter_setup
}

%prep
%setup -q -n %{oname}-%{version}
%patch1 -p0

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitearch}
%exclude %{python_sitearch}/simpleparse/tests
%exclude %{python_sitearch}/simpleparse/examples
%doc license.txt doc examples

%changelog
* Wed Aug 17 2011 Andy Grover <agrover@redhat.com> - 2.1.1-3
- Add patch to fix some missing EOLs

* Wed Aug 17 2011 Andy Grover <agrover@redhat.com> - 2.1.1-2
- Filter out mxtexttools.so provides

* Tue Aug 16 2011 Andy Grover <agrover@redhat.com> - 2.1.1-1
- Update to latest upstream version
- Modify URL and Source
- Remove mx dependency

* Tue May 10 2011 Andy Grover <agrover@redhat.com> - 2.0.0-1
- Initial packaging
