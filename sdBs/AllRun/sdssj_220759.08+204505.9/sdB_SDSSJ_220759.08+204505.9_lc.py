from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[331.996167,20.751639], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_220759.08+204505.9 /sdB_SDSSJ_220759.08+204505.9_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
