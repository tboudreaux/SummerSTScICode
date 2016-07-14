from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[354.391667,43.7795],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_233734.00+434646.2/sdB_sdssj_233734.00+434646.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_233734.00+434646.2/sdB_sdssj_233734.00+434646.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
