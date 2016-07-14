from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[322.275125,0.752556], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_212906.03+004509.2 /sdB_SDSSJ_212906.03+004509.2_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
