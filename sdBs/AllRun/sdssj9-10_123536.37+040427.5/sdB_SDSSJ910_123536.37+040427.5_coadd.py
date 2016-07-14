from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[188.901542,4.074306],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_123536.37+040427.5/sdB_SDSSJ910_123536.37+040427.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_123536.37+040427.5/sdB_SDSSJ910_123536.37+040427.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()