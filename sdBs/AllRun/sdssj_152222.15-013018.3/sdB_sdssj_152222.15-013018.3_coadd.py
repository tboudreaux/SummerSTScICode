from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[230.592292,-1.505083],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_152222.15-013018.3/sdB_sdssj_152222.15-013018.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_152222.15-013018.3/sdB_sdssj_152222.15-013018.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
