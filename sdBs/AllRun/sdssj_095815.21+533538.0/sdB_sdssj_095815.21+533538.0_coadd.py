from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[149.563375,53.593889],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_095815.21+533538.0/sdB_sdssj_095815.21+533538.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_095815.21+533538.0/sdB_sdssj_095815.21+533538.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
