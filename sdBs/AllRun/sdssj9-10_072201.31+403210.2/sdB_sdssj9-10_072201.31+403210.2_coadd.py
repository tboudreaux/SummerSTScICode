from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[110.505458,40.536167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_072201.31+403210.2/sdB_sdssj9-10_072201.31+403210.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_072201.31+403210.2/sdB_sdssj9-10_072201.31+403210.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
