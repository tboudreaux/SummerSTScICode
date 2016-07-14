from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[317.770708,9.178583], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_211104.97+091042.9 /sdB_SDSSJ_211104.97+091042.9_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
