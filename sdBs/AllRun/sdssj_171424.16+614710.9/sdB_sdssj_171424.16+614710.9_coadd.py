from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[258.600667,61.786361],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_171424.16+614710.9/sdB_sdssj_171424.16+614710.9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_171424.16+614710.9/sdB_sdssj_171424.16+614710.9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
