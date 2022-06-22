# -*- coding: utf-8 -*-

import ipywidgets as ipw

template = """
<div align="center">
    <img src="{appbase}/atmospec_logo-01.png" height="128px" width=453px">
</div>
<table>
<tr>
  <th style="text-align:center">ISPG testing Applications</th>
<tr>
  <td valign="top"><ul>
    <li><a href="{appbase}/example.ipynb" target="_blank">Notebook prototyping</a></li>
  </ul></td>
  <td valign="top"><ul>
    <li><a href="{appbase}/spectrum_widget.ipynb" target="_blank">Spectrum Widget</a></li>
  </ul></td>
  <td valign="top"><ul>
    <li><a href="{appbase}/conformer_generation.ipynb" target="_blank">Conformer Widget</a></li>
  </ul></td>
  <td valign="top"><ul>
    <li><a href="{appbase}/orca_optimization.ipynb" target="_blank">NEA UV/VIS spectrum</a></li>
  </ul></td>
</tr>
</table>
"""


def get_start_widget(appbase, jupbase, notebase):
    html = template.format(appbase=appbase, jupbase=jupbase, notebase=notebase)
    return ipw.HTML(html)


# EOF
