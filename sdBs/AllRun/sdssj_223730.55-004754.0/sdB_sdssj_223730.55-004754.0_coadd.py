from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[339.377292,0.798333],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_223730.55-004754.0/sdB_sdssj_223730.55-004754.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_223730.55-004754.0/sdB_sdssj_223730.55-004754.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
