from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[230.533375,34.417444],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_152208.01+342502.8/sdB_SDSSJ910_152208.01+342502.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_152208.01+342502.8/sdB_SDSSJ910_152208.01+342502.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
