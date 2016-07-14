from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[242.156667,43.130222],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_160837.60+430748.8/sdB_SDSSJ910_160837.60+430748.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_160837.60+430748.8/sdB_SDSSJ910_160837.60+430748.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
