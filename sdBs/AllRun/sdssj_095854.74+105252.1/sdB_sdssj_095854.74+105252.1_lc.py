from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[149.728083,10.881139], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_095854.74+105252.1/sdB_sdssj_095854.74+105252.1_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
