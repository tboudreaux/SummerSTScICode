from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[261.836583,32.819028], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_172720.78+324908.5/sdB_sdssj_172720.78+324908.5_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
