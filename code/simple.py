
def search_nearest(x, vals, root_num, delta):
    assert pow(vals[1], root_num) > x
    assert pow(vals[0], root_num) < x

    max_step = 10000
    p = [0.0]*2

    step = 0
    while(True):
        step += 1

        v_mid = (vals[0] + vals[1]) / 2.0
        p_mid = pow(v_mid, root_num)
        if abs(p_mid - x) < delta or step >= max_step:
            break

        p[0] = pow(vals[0], root_num)
        p[1] = pow(vals[1], root_num)

        if p_mid > x:
            vals[1] = v_mid
        else:
            vals[0] = v_mid

        print("#%d, value: %10f, [%10f, %10f], p_mid: %10f\n" % (step, v_mid, vals[0], vals[1], p_mid))

    if(step == max_step):
        print("max step reached")



def main():
    search_nearest(2.0, [1.0, 1.5], 12, 0.0000000001)
	


if __name__ == "__main__":
	main()
