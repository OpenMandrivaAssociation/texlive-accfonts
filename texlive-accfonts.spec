%global tl_name accfonts
%global tl_revision 18835
%global tl_bin_links mkt1font:%{_texmfdistdir}/scripts/accfonts/mkt1font vpl2ovp:%{_texmfdistdir}/scripts/accfonts/vpl2ovp vpl2vpl:%{_texmfdistdir}/scripts/accfonts/vpl2vpl

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
BuildSystem:	texlive
Requires:	texlive(accfonts.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

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

