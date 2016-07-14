Name:     ocaml-cry

Version:  0.4.1
Release:  1
Summary:  OCaml icecast/shoutcast lib
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-cry
Source0:  https://github.com/savonet/ocaml-cry/releases/download/0.4.1/ocaml-cry-0.4.1.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-bytes

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export OCAMLFIND_LDCONF=ignore
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
make install

%files
/usr/lib64/ocaml/cry/META
/usr/lib64/ocaml/cry/cry.a
/usr/lib64/ocaml/cry/cry.cma
/usr/lib64/ocaml/cry/cry.cmi
/usr/lib64/ocaml/cry/cry.cmx
/usr/lib64/ocaml/cry/cry.cmxa
/usr/lib64/ocaml/cry/cry.mli
/usr/lib64/ocaml/cry/cry_ssl.cmi
/usr/lib64/ocaml/cry/cry_ssl.cmx

%description
OCaml low level implementation of the shout protocol.

%changelog
* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-cry.spec
