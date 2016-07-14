from gPhoton.gAperture import gAperture
def main():
	gAperture(band="NUV", skypos=[332.08125,6.04875], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_SDSSJ_220819.50+060255.5 /sdB_SDSSJ_220819.50+060255.5_lc.csv", maxgap=1000., overwrite=True, radius=0.00555556, annulus=[0.005972227,0.0103888972], verbose=3)
if __name__ == "__main__":
	main()
