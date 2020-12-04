%define debug_package %{nil}

Name:     ocaml-cry
Version:  0.6.5
Release:  0.1%{dist}
Summary:  OCaml icecast/shoutcast lib

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:  GPLv2+
URL:      https://github.com/savonet/ocaml-cry
Source0:  https://github.com/savonet/ocaml-cry/archive/%{version}.tar.gz?#%{name}-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-dune

%description
OCaml low level implementation of the shout protocol.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}

%build
dune build

%install
dune install \
  --prefix %{buildroot} \
  --libdir %{buildroot}$(ocamlfind printconf destdir) \
  --mandir %{buildroot}/usr/share/doc/%{name}
rm -rf %{buildroot}/doc

%files
%doc README.md CHANGES
%license COPYING
%{_libdir}/ocaml/%{libname}
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%exclude %{_libdir}/ocaml/%{libname}/*.mli
%endif

%files devel
%license COPYING
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.mli
%endif

%changelog
* Thu Dec 3 2020 Lucas Bickel <hairmare@rabe.ch> - 0.6.5-0.1
- Bump to 0.6.5

* Sat Aug  3 2019 Lucas Bickel <hairmare@rabe.ch> - 0.6.3-0.0
- Bump to 0.6.3

* Sun Dec  9 2018 Lucas Bickel <hairmare@rabe.ch> - 0.6.2-0.1
- Clean up specfile and add seperate -devel package

* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.6.2-0.0
- Clean up Release tag
- Fix Fedora Rawhide build

* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch> - 0.4.1-1
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-cry.spec
