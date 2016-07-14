from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[123.476417,0.642667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_081354.34-003833.6/sdB_sdssj_081354.34-003833.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_081354.34-003833.6/sdB_sdssj_081354.34-003833.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
