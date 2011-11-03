# revision 18835
# category Package
# catalog-ctan /fonts/utilities/accfonts
# catalog-date 2009-04-10 11:27:58 +0200
# catalog-license gpl
# catalog-version 0.25
Name:		texlive-accfonts
Version:	0.25
Release:	1
Summary:	Utilities to derive new fonts from existing ones
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/utilities/accfonts
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/accfonts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/accfonts.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-accfonts.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The accfonts package contains three utilities to permit easy
manipulation of fonts, in particular the creation of unusual
accented characters. Mkt1font works on Adobe Type 1 fonts,
vpl2vpl works on TeX virtual fonts and vpl2ovp transforms a TeX
font to an Omega one. All three programs read in a font (either
the font itself or a property list), together with a simple
definition file containing lines such as '128 z acute'; they
then write out a new version of the font with the requested new
characters in the numerical slots specified. Great care is
taken over the positioning of accents, and over the provision
of kerning information for new characters; mkt1font also
generates suitable "hints" to enhance quality at small sizes or
poor resolutions. The programs are written in Perl.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/mkt1font
%{_bindir}/vpl2ovp
%{_bindir}/vpl2vpl
%{_texmfdistdir}/scripts/accfonts/mkt1font
%{_texmfdistdir}/scripts/accfonts/vpl2ovp
%{_texmfdistdir}/scripts/accfonts/vpl2vpl
%{_texmfdistdir}/tex/latex/accfonts/CSX.def
%{_texmfdistdir}/tex/latex/accfonts/ISO-Latin1.def
%{_texmfdistdir}/tex/latex/accfonts/ISO-Latin2.def
%{_texmfdistdir}/tex/latex/accfonts/IndUni_Omega.def
%{_texmfdistdir}/tex/latex/accfonts/Norman.def
%doc %{_texmfdistdir}/doc/fonts/accfonts/CHANGES
%doc %{_texmfdistdir}/doc/fonts/accfonts/COPYING
%doc %{_texmfdistdir}/doc/fonts/accfonts/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/accfonts/mkt1font mkt1font
    ln -sf %{_texmfdistdir}/scripts/accfonts/vpl2ovp vpl2ovp
    ln -sf %{_texmfdistdir}/scripts/accfonts/vpl2vpl vpl2vpl
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
