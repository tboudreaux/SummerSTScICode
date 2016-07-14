from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[252.2365,39.148917],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_164856.76+390856.1/sdB_sdssj_164856.76+390856.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_164856.76+390856.1/sdB_sdssj_164856.76+390856.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
