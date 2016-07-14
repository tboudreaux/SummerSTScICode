from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[260.587708,29.408722],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_172221.05+292431.4/sdB_SDSSJ910_172221.05+292431.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_172221.05+292431.4/sdB_SDSSJ910_172221.05+292431.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
