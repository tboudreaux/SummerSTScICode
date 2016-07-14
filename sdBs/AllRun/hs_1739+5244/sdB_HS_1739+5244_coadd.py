from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[265.108042,52.718856],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HS_1739+5244/sdB_HS_1739+5244_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HS_1739+5244/sdB_HS_1739+5244_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
