from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[327.724333,13.280694], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_215053.84+131650.5 /sdB_SDSSJ_215053.84+131650.5_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
