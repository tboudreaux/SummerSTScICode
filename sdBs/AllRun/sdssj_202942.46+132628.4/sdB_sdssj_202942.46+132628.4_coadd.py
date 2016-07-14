from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[307.426917,13.441222],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_202942.46+132628.4/sdB_sdssj_202942.46+132628.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_202942.46+132628.4/sdB_sdssj_202942.46+132628.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
