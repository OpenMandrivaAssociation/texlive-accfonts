%global tl_name accfonts
%global tl_revision 18835

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.25
Release:	%{tl_revision}.1
Summary:	Utilities to derive new fonts from existing ones
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/utilities/accfonts
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/accfonts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/accfonts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(accfonts.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The accfonts package contains three utilities to permit easy
manipulation of fonts, in particular the creation of unusual accented
characters. Mkt1font works on Adobe Type 1 fonts, vpl2vpl works on TeX
virtual fonts and vpl2ovp transforms a TeX font to an Omega one. All
three programs read in a font (either the font itself or a property
list), together with a simple definition file containing lines such as
'128 z acute'; they then write out a new version of the font with the
requested new characters in the numerical slots specified. Great care is
taken over the positioning of accents, and over the provision of kerning
information for new characters; mkt1font also generates suitable "hints"
to enhance quality at small sizes or poor resolutions. The programs are
written in Perl.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist/doc
%dir %{_datadir}/texmf-dist/texmf-dist/scripts
%dir %{_datadir}/texmf-dist/texmf-dist/tex
%dir %{_datadir}/texmf-dist/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/texmf-dist/scripts/accfonts
%dir %{_datadir}/texmf-dist/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/texmf-dist/doc/fonts/accfonts
%dir %{_datadir}/texmf-dist/texmf-dist/tex/latex/accfonts
%doc %{_datadir}/texmf-dist/texmf-dist/doc/fonts/accfonts/CHANGES
%doc %{_datadir}/texmf-dist/texmf-dist/doc/fonts/accfonts/COPYING
%doc %{_datadir}/texmf-dist/texmf-dist/doc/fonts/accfonts/README
%{_datadir}/texmf-dist/texmf-dist/scripts/accfonts/mkt1font
%{_datadir}/texmf-dist/texmf-dist/scripts/accfonts/vpl2ovp
%{_datadir}/texmf-dist/texmf-dist/scripts/accfonts/vpl2vpl
%{_datadir}/texmf-dist/texmf-dist/tex/latex/accfonts/CSX.def
%{_datadir}/texmf-dist/texmf-dist/tex/latex/accfonts/ISO-Latin1.def
%{_datadir}/texmf-dist/texmf-dist/tex/latex/accfonts/ISO-Latin2.def
%{_datadir}/texmf-dist/texmf-dist/tex/latex/accfonts/IndUni_Omega.def
%{_datadir}/texmf-dist/texmf-dist/tex/latex/accfonts/Norman.def
