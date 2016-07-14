from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[261.512375,31.106833],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_172602.97+310624.6/sdB_SDSSJ910_172602.97+310624.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_172602.97+310624.6/sdB_SDSSJ910_172602.97+310624.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
