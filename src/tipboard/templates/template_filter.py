from django import template
from django.template.loader import render_to_string
from src.tipboard.app.properties import ALLOWED_TILES

register = template.Library()


def isChartJS_tile(tile_template):
    return tile_template in ['bar_chart', 'vbar_chart', 'pie_chart', 'polararea_chart',
                             'doughnut_chart', 'half_doughnut_chart', 'radar_chart',
                             'cumulative_flow', 'norm_chart', 'line_chart']


@register.filter(name='template_tile_dashboard')
def template_tile_dashboard(tile_id, layout_name):
    """
        Many thanks to for the solution
        For detail, see Stackoverflow answer: https://stackoverflow.com/a/24402622/4797299
    """
    return tile_id, layout_name


@register.filter(name='template_tile_data')
def template_tile_data(packedData, tile_data):
    """
     this is the template to string render, of the tiles template in config.yaml
    :param packedData: (id of title
    :param tile_data: data to be send to the template tile
    :return: a string, representing the html generated by the tile template
    """
    tile_id, layout_name = packedData
    print(f'(DEBUG) new tile name: old({tile_id}) new({layout_name}-{tile_id})')
    data = dict(tile_id=f'{layout_name}-{tile_id}',
                tile_template=tile_data['tile_template'],
                title=tile_data['title'])
    if isinstance(tile_data, dict) and tile_data['tile_template'] in ALLOWED_TILES:
        if isChartJS_tile(tile_data['tile_template']):
            return render_to_string(f'tiles/chartJS_template.html', data)
        return render_to_string(f'tiles/{tile_data["tile_template"]}.html', data)
    data['reason'] = 'not found'
    return render_to_string(f'tiles/notfound_tiles.html', data)
