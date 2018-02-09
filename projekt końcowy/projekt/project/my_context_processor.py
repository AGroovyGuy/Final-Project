from datetime import datetime


def my_cp(request):
    ctx = {
        "version": "Względnie działająca",
        "actual_date": datetime.now(),
        "background": request.session.get("background", "white"),
        "fontcolor": request.session.get("fontcolor", "black"),
        "fontsize": request.session.get("fontsize", "12px"),
    }
    return ctx