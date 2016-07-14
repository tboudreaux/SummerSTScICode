from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[245.950417,17.717417],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_162348.10+174302.7/sdB_sdssj9-10_162348.10+174302.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_162348.10+174302.7/sdB_sdssj9-10_162348.10+174302.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
