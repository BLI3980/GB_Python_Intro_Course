# import model_sum as sum
# import model_sub as sub
import model_mult as mult
# import model_sqrt as sqrt
import view


# def button_click():
#     value_a = view.get_value()
#     value_b = view.get_value()
#     model.init(value_a, value_b)
#     result = model.sum()
#     view.view_data(result)


def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    # sum.init(value_a, value_b)
    # sub.init(value_a, value_b)
    mult.init(value_a, value_b)
    # sqrt.init(value_a, value_b)
    result = mult.calc()
    view.view_data(result, 'result')
