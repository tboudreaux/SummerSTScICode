from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[239.118083,1.226389], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_sdssj_155628.34+011335.0/sdB_sdssj_155628.34+011335.0_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
